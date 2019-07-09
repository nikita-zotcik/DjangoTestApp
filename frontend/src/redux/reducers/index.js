import {GET_ALL_COMPANIES, GET_ALL_OFFICES, GET_OFFICE} from "../constants";

const initialState = {
    offices: [],
    companies: []
};

function rootReducer(state = initialState, action) {
    if (action.type === GET_OFFICE) {
        return state.offices.find((office) => {
            return office.id === action.payload.id
        });
    }
    if (action.type === GET_ALL_OFFICES) {
        state.offices.push(action.payload)
    }
    if (action.type === GET_ALL_COMPANIES) {
        return  {
               ...state.offices,
                companies: action.payload
        }
    }
    return state
}

export default rootReducer;