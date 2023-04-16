from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()


class model_input(BaseModel):
    GrossFloorArea: float
    State: int
    OwnerTypes: int
    ProjectTypes: int


# loading the saved model
leed_model = pickle.load(open('LEED_Model.sav', 'rb'))


@app.post('/LEED_prediction')
def leed_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    GrossFloorArea = input_dictionary['GrossFloorArea']
    State = input_dictionary['State']
    OwnerTypes = input_dictionary['OwnerTypes']
    ProjectTypes = input_dictionary['ProjectTypes']

    input_list = [GrossFloorArea,State,OwnerTypes,ProjectTypes]

    prediction = leed_model.predict([input_list])
    return prediction[0]

