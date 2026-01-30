from typing import Dict, Any
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from data import load_data, split_data
from utils import load_model, save_model, get_model_info
from models import ModelRetraining

class AllModelService:
    
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model_metrics: Dict[str, Any] = {}
    
    def get_model_info(self) -> Dict[str, Any]:
        return get_model_info(self.model_path, self.model_metrics)
    
    def get_model_metrics(self) -> Dict[str, Any]:
        if not self.model_metrics:
            self.calculate_metrics()
        return self.model_metrics
    
    def calculate_metrics(self):
        model = load_model(self.model_path)
        X, y = load_data()
        _, X_test, _, y_test = split_data(X, y)
        y_pred = model.predict(X_test)
        
        self.model_metrics['accuracy'] = accuracy_score(y_test, y_pred)
        self.model_metrics['classification_report'] = classification_report(y_test, y_pred, output_dict=True)
   
    def model_retraining(self, retrain_params: ModelRetraining) -> Dict[str, Any]:
        X, y = load_data()
        X_train, X_test, y_train, y_test = split_data(X, y)
        
        decision_tree_classfier = DecisionTreeClassifier(
            max_depth=retrain_params.max_depth, 
            random_state=retrain_params.random_state
        )
        decision_tree_classfier.fit(X_train, y_train)
        
        save_model(decision_tree_classfier, self.model_path)
        
        y_pred = decision_tree_classfier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        self.model_metrics['accuracy'] = accuracy
        self.model_metrics['classification_report'] = classification_report(y_test, y_pred, output_dict=True)
        
        return {
            "message": "Model retraining done successfully",
            "accuracy": accuracy,
            "parameters": retrain_params.model_dump()
        }
    
    