import React, {Component} from 'react';
import {connect} from 'react-redux'
import {addCompanyForOffice, addNewCompany, fetchOfficesByCompany, setNewHeadquarter} from "../../API";
import Company from "../Company";
import './index.css'
import Input from "@material-ui/core/Input";
import Box from "@material-ui/core/Box";
import InputLabel from "@material-ui/core/InputLabel";
import Typography from "@material-ui/core/Typography";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableCell from "@material-ui/core/TableCell";
import TableBody from "@material-ui/core/TableBody";
import Table from "@material-ui/core/Table";
import Button from "@material-ui/core/Button";


const mapStateToProps = (state, ownProps) => {
    return {
        company: state.companies.filter((company) => {
            return company.id === parseInt(ownProps.match.params.id)
        })
    }
};

class CompanyOffices extends Component {

    constructor(props) {
        super(props);
        this.state = {
            officesData: null,
            showAddForm: false,
            formData: {
                city: '',
                country: '',
                street: '',
                postalCode: '',
                monthlyRent: '',
            }
        }
    }


    onInputChange(e) {
        const {id, value} = e.target;
        this.setState({
            ...this.state,
            formData: {
                ...this.state.formData,
                [id]: value
            }
        })
    }

    handleSubmit(e) {

        const {formData} = this.state;
        addCompanyForOffice(formData, this.props.company[0].id)
            .then((response) => {
                console.log(response)
            })
            .catch((error) => {
                console.log(error)
            })
    }


    componentDidMount() {
        fetchOfficesByCompany(this.props.match.params.id)
            .then((response) => {
                this.setState({
                    officesData: response.data
                })
            }).catch((error) => {
            console.log(error)
        })
    }


    setHeadquarter(id) {
        const company_id = this.props.company[0].id;
        setNewHeadquarter(id, this.props.company[0].id, this.props.company[0].name)
            .then((response) => {
                this.setState({
                    officesData: {
                        total_rent: this.state.officesData.total_rent,
                        offices: this.state.officesData.offices.map((office) => {
                            office.headquarter_of = null;
                            if (office.id === id) {
                                office.headquarter_of = company_id
                            }
                            return office
                        })
                    }
                })
            })
            .catch((error) => {
                console.log(error)
            })
    }

    render() {
        console.log(this.state);
        console.log(this.props);
        // console.log(this.props);
        return (
            <Box m={3} component="div" display="block">
                <Box align={"left"}>
                    <Button href={"/"}>
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
                            <path d="M15 8.25H5.87l4.19-4.19L9 3 3 9l6 6 1.06-1.06-4.19-4.19H15v-1.5z"/>
                        </svg>
                    </Button>
                </Box>
                {this.props.company[0] && this.state.officesData ? (
                    (
                        <React.Fragment>
                            <Typography
                                variant={"h4"}
                                color={"testPrimary"}
                                align={"center"}>{this.props.company[0].name}</Typography>

                            <Typography variant={"subtitle1"} align={"center"}>Total
                                Rent: {this.state.officesData.total_rent}</Typography>
                            <Table>
                                <TableHead>
                                    <TableRow>
                                        <TableCell>Country</TableCell>
                                        <TableCell>City</TableCell>
                                        <TableCell>Postal Code</TableCell>
                                        <TableCell>Street</TableCell>
                                        <TableCell>Monthly Rent</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {this.state.officesData.offices.map((office, index) => {
                                        return (
                                            <TableRow key={index}>
                                                <TableCell>{office.country}</TableCell>
                                                <TableCell>{office.city}</TableCell>
                                                <TableCell>{office.street}</TableCell>
                                                <TableCell>{office.postalCode}</TableCell>
                                                <TableCell>{office.monthly_rent}</TableCell>
                                                {!office.headquarter_of && (
                                                    <TableCell>
                                                        <Button
                                                            onClick={() => this.setHeadquarter(office.id)}
                                                            className={"headquarter"}>Set as Headquarter
                                                        </Button>
                                                    </TableCell>)
                                                }

                                            </TableRow>
                                        )
                                    })}
                                </TableBody>
                            </Table>
                            <Box m={3}>
                                <Button variant="contained" color="primary" className={"AddButton"}
                                        onClick={e => this.setState({showAddForm: true})}>Add New
                                    Company
                                </Button>
                            </Box>
                            {this.state.showAddForm &&
                            (
                                <form className={"addCompanyForm"} onSubmit={this.handleSubmit.bind(this)}>
                                    <em>Office data:</em>
                                    <br/>
                                    <Box m={1}>
                                        <InputLabel required={true} htmlFor="country">Country</InputLabel>
                                        <Input required={true} type="text" id={"country"} value={this.state.formData.country}
                                               onChange={this.onInputChange.bind(this)}/>
                                    </Box>

                                    <Box m={1}>
                                        <InputLabel required={true} htmlFor="city">City</InputLabel>
                                        <Input required={true} type="text" id={"city"} value={this.state.formData.city}
                                               onChange={this.onInputChange.bind(this)}/>
                                    </Box>
                                    <Box m={1}> <InputLabel required={true} htmlFor="street">Street</InputLabel>
                                        <Input required={true} type="text" id={"street"} value={this.state.formData.street}
                                               onChange={this.onInputChange.bind(this)}/></Box>
                                    <Box m={1}><InputLabel required={true} htmlFor="postalCode">Postal Code</InputLabel>
                                        <Input required={true} type="text" id={"postalCode"} value={this.state.formData.postalCode}
                                               onChange={this.onInputChange.bind(this)}/></Box>
                                    <Box m={1}><InputLabel required={true} htmlFor="monthlyRent">Monthly Rent</InputLabel>
                                        <Input required={true} type="number" id={"monthlyRent"} value={this.state.formData.monthlyRent}
                                               onChange={this.onInputChange.bind(this)}/></Box>
                                    <Box m={1}>
                                        <Input type="submit" value="Submit"/>
                                    </Box>
                                </form>
                            )
                            }
                        </React.Fragment>
                    )
                ) : ''}


            </Box>
        )
    }
};

const companyOfficesListConnected = connect(mapStateToProps)(CompanyOffices);

export default companyOfficesListConnected