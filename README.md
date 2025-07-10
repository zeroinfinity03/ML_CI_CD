# 🎓 ML Student Performance Prediction

A modern machine learning project for predicting student performance using industry-standard tools and deployment practices.

## 🚀 **Modern Tech Stack**

- **⚡ Package Management**: `uv` (2024-2025 industry standard)
- **🐍 Python**: 3.11 (latest stable)
- **🤖 ML Libraries**: scikit-learn, XGBoost, CatBoost
- **🌐 Web Framework**: FastAPI
- **🐳 Containerization**: Docker
- **☁️ Multi-Cloud Deployment**: AWS ECS + Azure Container Apps (Docker)
- **🔄 CI/CD**: GitHub Actions

## 📁 **Project Structure**

```
ml-project/
├── 📦 pyproject.toml          # Modern dependency management
├── 🔒 uv.lock                 # Locked dependencies
├── 🐍 .python-version         # Python version (3.11)
├── 🐳 Dockerfile              # Container configuration
├── 🐳 docker-compose.yml      # Universal container configuration
├── 📝 app.py                  # FastAPI web application
├── 📝 main.py                 # Entry point
├── 📁 src/                    # ML pipeline source code
│   ├── components/            # ML components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/              # ML pipeline
│   │   └── predict_pipeline.py
│   └── utils.py               # Utility functions
├── 📁 artifacts/              # Trained models & data
├── 📁 notebook/               # Jupyter notebooks
├── 📁 templates/              # HTML templates
└── 📁 .github/workflows/      # CI/CD pipelines
    ├── aws-deploy.yml         # AWS deployment
    └── azure-deploy.yml       # Azure deployment
```

## 🛠️ **Quick Start**

### 1. **Install uv (Modern Python Package Manager)**
```bash
# macOS & Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.sh | iex"
```

### 2. **Setup Project**
```bash
# Clone repository
git clone <your-repo-url>
cd ml-project

# Install all dependencies automatically (creates .venv + installs packages)
uv sync

# All ML packages (pandas, scikit-learn, xgboost, etc.) are now installed!
```

### 3. **Run Locally**
```bash
# Run FastAPI application
uv run python app.py

# Or run with uvicorn
uv run uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Visit: `http://localhost:8000`

## 🐳 **Docker Setup**

### **Option 1: Docker Compose (Recommended)**
```bash
# Start application with all services
docker-compose up

# Run in background
docker-compose up -d

# Stop application
docker-compose down

# Access application
curl http://localhost:8000
```

### **Option 2: Manual Docker Build**
```bash
# Build Docker image
docker build -t ml-project .

# Run container
docker run -p 8000:8000 ml-project
```

### **Container Features:**
- ✅ Python 3.11 + uv for fast dependency installation
- ✅ OpenMP support for XGBoost/CatBoost
- ✅ All ML packages pre-installed
- ✅ Works on AWS, Azure, and local development

## ☁️ **Multi-Cloud Deployment**

### 🚀 **AWS Deployment (Production)**

**Automatic Deployment:**
```bash
# Push to main branch triggers AWS deployment
git push origin main
```

**Manual Deployment:**
1. Go to GitHub → Actions → "Deploy ML Project to AWS ECS"
2. Click "Run workflow"

**AWS Architecture:**
```
GitHub → Docker Build → AWS ECR → ECS/Fargate → Load Balancer
```

**AWS Setup Required:**
- ECR Repository: `ml-project`
- ECS Cluster: `ml-project-cluster`
- ECS Service: `ml-project-service`
- IAM Role: `ecsTaskExecutionRole`

### 🌐 **Azure Deployment (Development)**

**Automatic Deployment:**
```bash
# Push to azure-deploy branch triggers Azure deployment
git checkout -b azure-deploy
git push origin azure-deploy
```

**Manual Deployment:**
1. Go to GitHub → Actions → "Deploy ML Project to Azure (Docker)"
2. Click "Run workflow"

**Azure Architecture:**
```
GitHub → Docker Build → Azure Container Registry → Container Apps → Auto-scaling
```

## 🎯 **API Endpoints**

### **Main Endpoints:**
- `GET /` - Home page with prediction form
- `GET /predictdata` - Prediction form page
- `POST /predictdata` - Submit prediction request

### **Prediction API:**
```bash
# Example API call
curl -X POST "http://localhost:8000/predictdata" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "gender=male&ethnicity=group_a&parental_level_of_education=bachelor_degree&lunch=standard&test_preparation_course=completed&writing_score=75&reading_score=80"
```

## 📊 **Machine Learning Pipeline**

### **Models Trained:**
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

### **Features:**
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

### **Target:**
- Math Score Prediction



## 🌟 **Key Features**

### **Modern Development:**
- ⚡ **uv**: 10-100x faster than pip
- 🔒 **Locked Dependencies**: Reproducible builds
- 🐍 **Python 3.11**: Latest performance improvements
- 📦 **pyproject.toml**: Modern Python packaging

### **Production Ready:**
- 🐳 **Containerized**: Same environment everywhere
- 🔄 **CI/CD**: Automated deployment
- 📈 **Auto-scaling**: Handle traffic spikes

### **Multi-Cloud:**
- ☁️ **AWS**: Deploy to ECS/Fargate
- 🌐 **Azure**: Deploy to Container Apps
- 🖥️ **Local**: Run with Docker

## 📦 **Dependencies**

All ML and web framework dependencies are pre-configured in `pyproject.toml`:

### **Automatically Installed:**
```bash
# When you run 'uv sync', these packages are installed:
pandas>=2.3.1           # Data manipulation
numpy>=2.3.1            # Numerical computing  
scikit-learn>=1.7.0     # Machine learning
xgboost>=3.0.2          # Gradient boosting
catboost>=1.2.8         # Gradient boosting
matplotlib>=3.10.3      # Plotting
seaborn>=0.13.2         # Statistical visualization
fastapi>=0.116.0        # Web framework
uvicorn>=0.35.0         # ASGI server
dill>=0.4.0             # Model serialization
```

### **To Add More Packages:**
```bash
# Add new dependencies
uv add package-name

# Example: Add new ML library
uv add lightgbm
```

## 📈 **Deployment Strategies**

### **Recommended Usage:**

| Environment | Cloud | Branch | Use Case | Deployment Method |
|-------------|-------|---------|----------|------------------|
| **Development** | Azure | `azure-deploy` | Quick prototyping | 🐳 Docker Container |
| **Staging** | Azure | `azure-deploy` | Testing features | 🐳 Docker Container |
| **Production** | AWS | `main` | Live application | 🐳 Docker Container |
| **Multi-Cloud** | Both | Both branches | High availability | 🐳 Docker Container |

**🎯 All deployments use the SAME Dockerfile - industry standard approach!**

### **Branch Strategy:**
```bash
# Development workflow
git checkout -b feature/new-model
git push origin azure-deploy    # Deploy Docker container to Azure for testing

# Production workflow
git checkout main
git merge feature/new-model
git push origin main           # Deploy Docker container to AWS for production

# Both use the SAME Dockerfile - guaranteed consistency! 🎯
```

## 🔐 **Environment Variables**

### **GitHub Secrets (Required):**
```bash
# AWS Deployment (Docker → ECR → ECS)
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key

# Azure Deployment (Docker → ACR → Container Apps)
AZURE_REGISTRY_LOGIN_SERVER=your-registry.azurecr.io
AZURE_REGISTRY_USERNAME=your-username
AZURE_REGISTRY_PASSWORD=your-password
AZURE_RESOURCE_GROUP=your-resource-group
```

## 🔧 **Development Commands**

```bash
# Local development (no Docker)
uv run python app.py

# Docker development (recommended)
docker-compose up

# Add new dependencies
uv add package-name

# Update dependencies  
uv lock --upgrade

# Deploy to any cloud
docker-compose build  # Builds universal image
```

## 🤝 **Contributing**

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 **License**

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 **Acknowledgments**

- Built with modern Python tooling (uv, Python 3.11)
- Follows industry-standard MLOps practices
- Multi-cloud deployment architecture
- Production-ready containerization

---

---

**🚀 Ready to deploy! All dependencies included, Docker configured, CI/CD automated.**
