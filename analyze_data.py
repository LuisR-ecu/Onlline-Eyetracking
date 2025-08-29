import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def process_file(filepath: str) -> None:
    """Analyze a single Excel file and emit plots + CSVs next to it."""
    fname = os.path.basename(filepath)
    print(f"📄 Processing: {fname}")

    # Load per-instruction trial results
    try:
        results = pd.read_excel(filepath, sheet_name="Trial Results")
    except Exception as e:
        print(f"⚠️ No 'Trial Results' in {fname}: {e}")
        return

    required = {"rt", "version", "target", "success"}
    if not required.issubset(results.columns):
        print(f"⚠️ Skipping {fname}: 'Trial Results' missing required columns {sorted(required)}")
        return

    # Clean and export raw results
    results['rt'] = pd.to_numeric(results['rt'], errors='coerce')
    results['success'] = results['success'].astype(bool)
    raw_csv = filepath.replace('.xlsx', '_trial_results.csv')
    results.to_csv(raw_csv, index=False)
    print(f"✅ Raw trial results saved: {raw_csv}")

    # Filter successful trials with valid RT
    succ = results[results['success'] & results['rt'].notna()].copy()
    if succ.empty:
        print(f"⚠️ No successful trials with RT in {fname}")
        return

    # --- Graph 1: RT by picture number (1..4) ---
    plt.figure()
    ax = sns.barplot(data=succ, x='target', y='rt', estimator='mean', errorbar='ci', palette='Blues')
    ax.set_xlabel('Picture Number (Quadrant: 1=TL, 2=TR, 3=BL, 4=BR)')
    ax.set_ylabel('Reaction Time (s)')
    ax.set_title('Reaction Time by Picture Number (successful only)')
    plt.tight_layout()
    rt_by_target_path = filepath.replace('.xlsx', '_rt_by_target.png')
    plt.savefig(rt_by_target_path)
    print(f"✅ RT by target plot saved: {rt_by_target_path}")
    plt.close()

    # --- Graph 2: Clear vs Casual RT comparison ---
    ver_mean = succ.groupby('version')['rt'].mean().to_dict()
    mean_clear = ver_mean.get('clear')
    mean_casual = ver_mean.get('casual')

    if mean_clear is not None and mean_casual is not None and mean_casual > 0:
        improvement_pct = (mean_casual - mean_clear) / mean_casual * 100.0
    else:
        improvement_pct = None

    plt.figure()
    order = ['clear', 'casual'] if 'clear' in succ['version'].unique() else None
    ax = sns.barplot(data=succ, x='version', y='rt', order=order, estimator='mean', errorbar='ci', palette='Set2')
    ax.set_xlabel('Instruction Style')
    ax.set_ylabel('Reaction Time (s)')
    title = 'RT: Clear vs Casual'
    if improvement_pct is not None:
        title += f" (Clear faster by {improvement_pct:.1f}%)"
    ax.set_title(title)
    plt.tight_layout()
    cmp_path = filepath.replace('.xlsx', '_rt_clear_vs_casual.png')
    plt.savefig(cmp_path)
    print(f"✅ Clear vs casual RT plot saved: {cmp_path}")
    plt.close()

    # Save summary CSV with means and improvement percent
    summary_rows = []
    for v in ['clear', 'casual']:
        if v in ver_mean:
            summary_rows.append({'version': v, 'mean_rt': ver_mean[v]})
    summary_df = pd.DataFrame(summary_rows)
    if improvement_pct is not None:
        # Add a row for improvement
        summary_df = pd.concat([
            summary_df,
            pd.DataFrame([{'version': 'clear_vs_casual_improvement_pct', 'mean_rt': improvement_pct}])
        ], ignore_index=True)
    summary_csv = filepath.replace('.xlsx', '_rt_version_summary.csv')
    summary_df.to_csv(summary_csv, index=False)
    print(f"✅ Version RT summary saved: {summary_csv}")


def process_all(data_dir: str = "gaze_data") -> None:
    for fname in os.listdir(data_dir):
        if not fname.endswith(".xlsx"):
            continue
        process_file(os.path.join(data_dir, fname))


if __name__ == "__main__":
    process_all()
 