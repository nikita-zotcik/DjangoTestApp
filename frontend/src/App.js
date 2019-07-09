import React, {useEffect} from 'react';
import './App.css';
import CompaniesList from "./components/CompaniesList";
import CompanyOffices from "./components/CompanyOffices";
import {Route, BrowserRouter, Switch} from "react-router-dom";
import {fetchAllCompanies} from "./API";


function App() {
    useEffect(() => {
        fetchAllCompanies()
    }, []);
    return (
        <div className="App">
            <BrowserRouter>
                <Switch>
                    <Route path="/company/:id" component={CompanyOffices}/>
                    <Route path="/" component={CompaniesList}/>
                </Switch>
            </BrowserRouter>
        </div>
    );
}

export default App;