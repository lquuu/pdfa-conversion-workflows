import argparse
import pandas as pd
from pathlib import Path

def compare_single_row_csvs(original_filepath, converted_filepath, base_name, output_csv):
    """
    Purpose:
    Compares two single-row metadata CSV files (original vs converted)
    and produces a long-form comparison CSV.

    Behavior:
    - Computes the union of metadata fields
    - Classifies each field as:
        - Unchanged
        - Modified
        - Added in converted
        - Removed from original

    Intended Use:
    Called programmatically by run_pairs.ps1 as part of the
    DOCX → PDF/A metadata evaluation workflow.
    """


    orig = pd.read_csv(original_filepath, encoding="latin1")
    conv = pd.read_csv(converted_filepath, encoding="latin1")

    orig_dict = orig.iloc[0].to_dict()
    conv_dict = conv.iloc[0].to_dict()

    all_keys = sorted(set(orig_dict.keys()).union(conv_dict.keys()))

    results = []
    for key in all_keys:
        orig_val = orig_dict.get(key, "")
        conv_val = conv_dict.get(key, "")

        if (orig_val == "" or pd.isna(orig_val)) and (conv_val != "" and not pd.isna(conv_val)):
            status = "Added in converted"
        elif (orig_val != "" and not pd.isna(orig_val)) and (conv_val == "" or pd.isna(conv_val)):
            status = "Removed from original"
        elif str(orig_val) != str(conv_val):
            status = "Modified"
        else:
            status = "Unchanged"

        results.append({
            "BaseName": base_name,
            "Tag": key,
            "Original_Value": "" if pd.isna(orig_val) else orig_val,
            "Converted_Value": "" if pd.isna(conv_val) else conv_val,
            "Change_Status": status
        })

    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False, encoding="utf-8")
    return df

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orig_csv", required=True)
    ap.add_argument("--conv_csv", required=True)
    ap.add_argument("--base_name", required=True)
    ap.add_argument("--out_csv", required=True)
    args = ap.parse_args()

    compare_single_row_csvs(args.orig_csv, args.conv_csv, args.base_name, args.out_csv)
    print(f"✅ Wrote comparison: {args.out_csv}")

if __name__ == "__main__":
    main()
