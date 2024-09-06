import pickle
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.neighbors import NearestNeighbors

# Load the saved models
def load_models():
    kmeans_model_path = 'models/kmeans_model.pkl'
    pca_model_path = 'models/pca_model.pkl'
    scaler_model_path = 'models/scaler.pkl'
    multibinarizer_path = 'models/mlb_model.pkl'
    feature_names_path = 'models/feature_names.pkl'
    
    with open(kmeans_model_path, 'rb') as f:
        kmeans = pickle.load(f)
    with open(pca_model_path, 'rb') as f:
        pca = pickle.load(f)
    with open(scaler_model_path, 'rb') as f:
        scaler = pickle.load(f)
    with open(multibinarizer_path, 'rb') as f:
        multibin = pickle.load(f)
    with open(feature_names_path, 'rb') as f:
        feature_names = pickle.load(f)
    
    return kmeans, pca, scaler, multibin, feature_names

# Load DataFrame
df = pd.read_csv('data/survey_results_with_clusters.csv')

# Load models and feature names
kmeans, pca, scaler, multibin, feature_names = load_models()

# Multi-category features and single-entry features
multi_category_features = [
    'LanguageHaveWorkedWith', 'DatabaseHaveWorkedWith', 'PlatformHaveWorkedWith',
    'ToolsTechHaveWorkedWith', 'AISearchHaveWorkedWith', 'LearnCodeCoursesCert',
    'ProfessionalTech', 'AIDevHaveWorkedWith'
]

single_entry_features = ['DevType', 'EdLevel', 'Industry']

def preprocess_input_data(data):
    df_input = pd.DataFrame(data, columns=feature_names)
    
    print("Initial DataFrame:")
    print(df_input.head())

    # Numeric conversion
    df_input['YearsCodePro'] = pd.to_numeric(df_input['YearsCodePro'], errors='coerce').fillna(0)
    df_input['YearsCode'] = pd.to_numeric(df_input['YearsCode'], errors='coerce').fillna(0)

    print("After Numeric Conversion:")
    print(df_input.head())

    # MultiLabelBinarizer
    for col in multi_category_features:
        if col in df_input.columns:
            df_input[col] = df_input[col].apply(lambda x: x.split(';') if isinstance(x, str) else [])
            mlb_output = multibin.transform(df_input[col])
            mlb_df = pd.DataFrame(mlb_output, columns=[f"{col}_{cls}" for cls in multibin.classes_])
            df_input = pd.concat([df_input, mlb_df], axis=1).drop(columns=[col])

    print("After MultiLabelBinarizer:")
    print(df_input.head())

    # One-hot encoding
    df_input = pd.get_dummies(df_input, columns=single_entry_features)

    print("After One-hot Encoding:")
    print(df_input.head())

    # Ensure all columns match
    df_input = df_input.reindex(columns=feature_names, fill_value=0)

    print("After Reindexing:")
    print(df_input.head())

    # Scaling
    try:
        scaled_features = scaler.transform(df_input)
        print("Scaled Features Shape:", scaled_features.shape)
    except Exception as e:
        print(f"Scaling Error: {e}")
        raise

    # PCA
    try:
        pca_features = pca.transform(scaled_features)
        print("PCA Features Shape:", pca_features.shape)
    except Exception as e:
        print(f"PCA Error: {e}")
        raise

    return pca_features

# Streamlit interface
st.title('Job Recommendation System')

user_skills = st.text_input('Enter your skills (comma-separated):', '')
user_experience = st.number_input('Enter your years of experience:', min_value=0, step=1)

if st.button('Get Recommendations'):
    if user_skills:
        try:
            user_skills_list = [skill.strip() for skill in user_skills.split(',')]
            user_input = {
                'YearsCodePro': [user_experience],
                'YearsCode': [user_experience],
                **{col: [', '.join(user_skills_list)] for col in multi_category_features}
            }
            
            processed_input = preprocess_input_data(user_input)
            
            cluster_prediction = kmeans.predict(processed_input)
            
            filtered_df = df[df['Cluster'] == cluster_prediction[0]]
            filtered_pca_features = pca.transform(scaler.transform(filtered_df[feature_names].values))
            knn = NearestNeighbors(n_neighbors=5, metric='cosine')
            knn.fit(filtered_pca_features)
            distances, indices = knn.kneighbors(processed_input)
            
            recommendations = filtered_df.iloc[indices[0]].copy()
            recommendations['Confidence'] = 1 - distances[0]

            st.write('**Recommended Job Profiles:**')
            st.dataframe(recommendations[['DevType', 'Key Skills', 'YearsCodePro', 'Industry', 'Confidence']].sort_values(by='Confidence', ascending=False))
        except Exception as e:
            st.error(f'An error occurred: {e}')
    else:
        st.error('Please enter your skills.')
