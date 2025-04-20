from sklearn.tree import DecisionTreeClassifier

class ModelTrainer:
    @staticmethod
    def train_model(X_train, y_train, max_depth):
        model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)
        return model
