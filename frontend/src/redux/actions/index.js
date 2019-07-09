import {GET_OFFICE, GET_ALL_COMPANIES} from "../constants";

export const getOffice = (payload) => {
    return {type: GET_OFFICE, payload}
};

export const getAllCompanies = (payload) => {
    return {type: GET_ALL_COMPANIES, payload}
};
