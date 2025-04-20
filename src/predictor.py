import pandas as pd

class Predictor:
    @staticmethod
    def make_predictions(model, X_test):
        y_pred = model.predict(X_test)
        predictions_df = pd.DataFrame({
            'Wine ID': range(1, len(y_pred) + 1),
            'Predicted Quality': y_pred,
            'Predicted Label': pd.Series(y_pred).apply(lambda x: "Good" if x >= 5 else "Bad")
        })
        return predictions_df, y_pred
    # return dataframe & the raw predictions
