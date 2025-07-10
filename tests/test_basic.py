import pytest
import sys
import os
import pandas as pd

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pipeline.predict_pipeline import CustomData, PredictPipeline
from utils import save_object, load_object


class TestBasicFunctionality:
    """Basic tests to ensure the ML project components work correctly"""
    
    def test_custom_data_creation(self):
        """Test that CustomData class can be instantiated"""
        data = CustomData(
            gender="male",
            race_ethnicity="group A",
            parental_level_of_education="bachelor's degree",
            lunch="standard",
            test_preparation_course="completed",
            reading_score=75,
            writing_score=80
        )
        
        assert data.gender == "male"
        assert data.reading_score == 75
        assert data.writing_score == 80
    
    def test_custom_data_to_dataframe(self):
        """Test that CustomData can be converted to DataFrame"""
        data = CustomData(
            gender="female",
            race_ethnicity="group B",
            parental_level_of_education="master's degree",
            lunch="free/reduced",
            test_preparation_course="none",
            reading_score=85,
            writing_score=90
        )
        
        df = data.get_data_as_data_frame()
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 1
        assert df['gender'].iloc[0] == "female"
        assert df['reading_score'].iloc[0] == 85
        assert df['writing_score'].iloc[0] == 90
    
    def test_predict_pipeline_creation(self):
        """Test that PredictPipeline can be instantiated"""
        pipeline = PredictPipeline()
        assert pipeline is not None
    
    def test_artifacts_exist(self):
        """Test that required model artifacts exist"""
        model_path = os.path.join("artifacts", "model.pkl")
        preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
        
        assert os.path.exists(model_path), f"Model file not found at {model_path}"
        assert os.path.exists(preprocessor_path), f"Preprocessor file not found at {preprocessor_path}"
    
    def test_utils_functions(self):
        """Test utility functions work correctly"""
        import tempfile
        import os
        
        # Test save_object and load_object
        test_data = {"test": "data", "number": 42}
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pkl') as tmp:
            tmp_path = tmp.name
        
        try:
            # Test saving
            save_object(tmp_path, test_data)
            assert os.path.exists(tmp_path)
            
            # Test loading
            loaded_data = load_object(tmp_path)
            assert loaded_data == test_data
            
        finally:
            # Clean up
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


class TestAPIEndpoints:
    """Test API-related functionality"""
    
    def test_import_app(self):
        """Test that the main app can be imported"""
        sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
        
        try:
            import app
            assert hasattr(app, 'app')  # FastAPI app instance
        except ImportError:
            pytest.skip("App module not available for testing")
    
    def test_templates_exist(self):
        """Test that required templates exist"""
        template_files = ['templates/index.html', 'templates/home.html']
        
        for template_file in template_files:
            assert os.path.exists(template_file), f"Template {template_file} not found" 