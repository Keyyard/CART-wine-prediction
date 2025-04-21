import pandas as pd
import streamlit as st

class ComparisonTable:
    @staticmethod
    def create_comparison_table(y_test, y_pred):
        y_test = y_test.reset_index(drop=True)
        comparison_df = pd.DataFrame({
            'Wine ID': range(1, len(y_test) + 1),
            'Actual Quality': y_test.values,
            'Actual Label': y_test.apply(lambda x: "Good" if x >= 5 else "Bad"),
            'Predicted Quality': y_pred,
            'Predicted Label': pd.Series(y_pred).apply(lambda x: "Good" if x >= 5 else "Bad"),
            'Match': y_test.apply(lambda x: "Exact Match" if (x==y_pred[y_test.index.get_loc(x)]) else "Match" if ("Good" if x >= 5 else "Bad") == ("Good" if y_pred[y_test.index.get_loc(x)] >= 5 else "Bad") else "Mismatch")
        })
        return comparison_df

    @staticmethod
    def display_comparison_table(comparison_df):
        st.subheader("Detailed Comparison: Actual vs Predicted (Wine Quality)")
        st.write(comparison_df.style.applymap(
            lambda x: 'background-color: #5994bc' if x == 'Exact Match' else 'background-color: lightgreen' if x == 'Match' else 'background-color: lightcoral', subset=['Match']
        ).set_table_styles(
            [{'selector': 'th', 'props': [('font-size', '110%'), ('text-align', 'center')]}]
        ))
        

        csv = comparison_df.to_csv(index=False)
        st.download_button("Download Comparison Table", csv, "comparison_table.csv", "text/csv")
        

        exact_matches_count = comparison_df['Match'].value_counts().get("Exact Match", 0)
        st.write(f"Number of Exact Matches: {exact_matches_count}/{len(comparison_df)}")
