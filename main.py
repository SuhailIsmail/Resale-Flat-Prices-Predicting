import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import pickle



def town_mapping(town):

    if town == 'ANG MO KIO':
        town_1 = int(0)
    elif town == 'BEDOK':
        town_1 = int(1)
    elif town == 'BISHAN':
        town_1= int(2)
    elif town == 'BUKIT BATOK':
        town_1= int(3)
    elif town == 'BUKIT MERAH':
        town_1= int(4)
    elif town == 'BUKIT PANJANG':
        town_1= int(5)

    elif town == 'BUKIT TIMAH':
        town_1= int(6)
    elif town == 'CENTRAL AREA':
        town_1= int(7)
    elif town == 'CHOA CHU KANG':
        town_1= int(8)
    elif town == 'CLEMENTI':
        town_1= int(9)
    elif town == 'GEYLANG':
        town_1= int(10)
    
    elif town == 'HOUGANG':
        town_1 = int(11)
    elif town == 'JURONG EAST':
        town_1 = int(12)
    elif town == 'JURONG WEST':
        town_1 = int(13)
    elif town == 'KALLANG/WHAMPOA':
        town_1 = int(14)
    elif town == 'MARINE PARADE':
        town_1 = int(15)

    elif town == 'PASIR RIS':
        town_1 = int(16)
    elif town == 'PUNGGOL':
        town_1 = int(17)
    elif town == 'QUEENSTOWN':
        town_1 = int(18)
    elif town == 'SEMBAWANG':
        town_1 = int(19)
    elif town == 'SENGKANG':
        town_1 = int(20)

    elif town == 'SERANGOON':
        town_1 = int(21)
    elif town == 'TAMPINES':
        town_1 = int(22)
    elif town == 'TOA PAYOH':
        town_1 = int(23)
    elif town == 'WOODLANDS':
        town_1 = int(24)        
    elif town == 'YISHUN':
        town_1 = int(25)

    return town_1

def flat_model_mapping(fl_m):


    if fl_m == 'Improved':
        flat_model_1= int(0)
    elif fl_m == 'New Generation':
        flat_model_1= int(1)
        
    elif fl_m == 'Model A':
        flat_model_1= int(2)
    elif fl_m == 'Standard':
        flat_model_1= int(3)
    elif fl_m == 'Simplified':
        flat_model_1= int(4)
    elif fl_m == 'Premium Apartment':
        flat_model_1= int(5)
    elif fl_m == 'Maisonette':
        flat_model_1= int(6)

    elif fl_m == 'Apartment':
        flat_model_1= int(7)
    elif fl_m == 'Model A2':
        flat_model_1= int(8)
    elif fl_m == 'Type S1':
        flat_model_1= int(9)
    elif fl_m == 'Type S2':
        flat_model_1= int(10)
    elif fl_m == 'Adjoined flat':
        flat_model_1= int(11)

    elif fl_m == 'Terrace':
        flat_model_1= int(12)
    elif fl_m == 'DBSS':
        flat_model_1= int(13)
    elif fl_m == 'Model A-Maisonette':
        flat_model_1= int(14)
    elif fl_m == 'Premium Maisonette':
        flat_model_1= int(15)
    elif fl_m == 'Multi Generation':
        flat_model_1= int(16)

    elif fl_m == 'Premium Apartment Loft':
        flat_model_1= int(17)
    elif fl_m == 'Improved-Maisonette':
        flat_model_1= int(18)
    elif fl_m == '2-room':
        flat_model_1= int(19)
    elif fl_m == '3Gen':
        flat_model_1= int(20)
    
    return flat_model_1

def flat_type_mapping(fl_type):

    if fl_type == '1 ROOM':
        fl_type1 = int(0)
    if fl_type == '2 ROOM':
        fl_type1 = int(1)
    if fl_type == '3 ROOM':
        fl_type1 = int(2)
    if fl_type == '4 ROOM':
        fl_type1 = int(3)
    if fl_type == '5 ROOM':
        fl_type1 = int(4)
    if fl_type == 'EXECUTIVE':
        fl_type1 = int(5)
    if fl_type == 'MULTI-GENERATION':
        fl_type1 = int(6)

    return fl_type1

def predict_price(year,town,flat_type,flr_area_sqm,flat_model,stry_start,stry_end,re_les_year,
              re_les_month,les_coms_dt):
    
    year_1 = int(year)
    town_2 = town_mapping(town)
    flt_ty_2 = flat_type_mapping(flat_type)
    flr_ar_sqm_1 = int(flr_area_sqm)
    flt_model_2 = flat_model_mapping(flat_model)
    str_str = np.log(int(stry_start))
    str_end = np.log(int(stry_end))
    rem_les_year = int(re_les_year)
    rem_les_month = int(re_les_month)
    lese_coms_dt = int(les_coms_dt)

    with open(r"ResaleFlatPrices_model.pkl","rb") as f:
        regg_model = pickle.load(f)

    user_data = np.array([[year_1,town_2,flt_ty_2,flr_ar_sqm_1,flt_model_2,
                           str_str,str_end,rem_les_year,rem_les_month,lese_coms_dt]])
    y_pred = regg_model.predict(user_data)
    price = np.exp(y_pred[0])

    return round(price)

st.set_page_config(layout="wide")

st.title("SINGAPORE RESALE FLAT PRICES PREDICTING")
st.write("")

with st.sidebar:
    select = option_menu("Main Menu",["Home","Price Prediction","About"])

if select == "Home":
    st.header("HDB Flats:")

    st.write('''The majority of Singaporeans live in public housing provided by the HDB.
    HDB flats can be purchased either directly from the HDB as a new unit or through the resale market from existing owners.''')
    
    st.header("Resale Process:")

    st.write('''In the resale market, buyers purchase flats from existing flat owners, and the transactions are facilitated through the HDB resale process.
    The process involves a series of steps, including valuation, negotiations, and the submission of necessary documents.''')

elif select == "Price Prediction":
    col1,col2 = st.columns(2)
    with col1:

        year = st.selectbox("Select Year",["2015", "2016", "2017", "2018", "2019", "2020", "2021",
                           "2022", "2023", "2024"])
        
        town = st.selectbox("Select Town",['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                            'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                                            'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                            'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                                            'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                                            'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
        
        flat_type = st.selectbox("Select Flat_Type",['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM',
                                                        'MULTI-GENERATION'])
        
        flat_ar_sqm = st.number_input("Enter the value of Floor Area SQM (Min: 31/ Max:280")

        flat_model = st.selectbox("Select the Flat Model",['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
                                                        'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2',
                                                        'Type S1', 'Type S2', 'Adjoined flat', 'Terrace', 'DBSS',
                                                        'Model A-Maisonette', 'Premium Maisonette', 'Multi Generation',
                                                        'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen'])

    with col2:

        stry_start = st.number_input("Enter the value of Storey Start")
        stry_end = st.number_input("Enter the value of Storey End")    

        re_les_year = st.number_input("Enter the value of Remaining Lease Year (Min: 42/ Max: 97")
        re_les_month = st.number_input("Enter the value of Remaining Lease Month (Min: 0/ Max: 11")

        les_coms_date = st.selectbox("Select the Lease Commence Date",[str(i) for i in range (1966, 2023)])
    
    button = st.button("Predict the Price",use_container_width=True)

    if button:

        Pred_price = predict_price(year,town,flat_type,flat_ar_sqm,flat_model,stry_start,
                                stry_end,re_les_year,re_les_month,les_coms_date)
        
        st.write("## :green[**The Predicted Price is :**]",Pred_price)

elif select == "About":

    st.header(":blue[Data Collection and Preprocessing:]")
    st.write("Collect a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to Till Date. Preprocess the data to clean and structure it for machine learning.")

    st.header(":blue[Feature Engineering:]")
    st.write("Extract relevant features from the dataset, including town, flat type, storey range, floor area, flat model, and lease commence date. Create any additional features that may enhance prediction accuracy.")
    
    st.header(":blue[Model Selection and Training:]")
    st.write("Choose an appropriate machine learning model for regression (e.g., linear regression, decision trees, or random forests). Train the model on the historical data, using a portion of the dataset for training.")

    st.header(":blue[Model Evaluation:]")
    st.write("Evaluate the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE) and R2 Score.")

    st.header(":blue[Streamlit Web Application:]")
    st.write("Develop a user-friendly web application using Streamlit that allows users to input details of a flat (town, flat type, storey range, etc.). Utilize the trained machine learning model to predict the resale price based on user inputs.")

    st.header(":blue[Deployment on Render:]")
    st.write("Deploy the Streamlit application on the Render platform to make it accessible to users over the internet.")
    
    st.header(":blue[Testing and Validation:]")
    st.write("Thoroughly test the deployed application to ensure it functions correctly and provides accurate predictions.")

        