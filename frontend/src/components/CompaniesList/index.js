import React, {Component} from 'react';
import {connect} from 'react-redux'
import {addNewCompany, fetchAllCompanies} from "../../API";
import Company from "../Company";
import './index.css'
import Button from '@material-ui/core/Button';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from "@material-ui/core/InputLabel";
import Input from "@material-ui/core/Input";
import Box from "@material-ui/core/Box";
import Table from "@material-ui/core/Table";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableCell from "@material-ui/core/TableCell";
import TableBody from "@material-ui/core/TableBody";
import {FormGroup} from "@material-ui/core";


const mapStateToProps = (state, ownProps) => {
    return {
        companies: state.companies
    }
};

class CompaniesList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            showAddForm: false,
            formData: {
                name: '',
                city: '',
                country: '',
                street: '',
                postalCode: '',
                monthlyRent: '',
            },
            error: null,
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
        addNewCompany(formData)
            .then((response) => {
                console.log(response)
            })
            .catch((error) => {
                console.log(error)
            })

    }

    render() {
        return (
            <Box component="div" display="block">
                <Box component="div" display="block">
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell>Company Name</TableCell>
                                <TableCell>Head City</TableCell>
                                <TableCell>Head Street</TableCell>
                                <TableCell>Head Postal Code</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {
                                this.props.companies &&
                                this.props.companies.map((company, index) => {
                                    return <Company key={index} company={company}/>
                                })
                            }
                        </TableBody>
                    </Table>
                    <Box m={3}>
                        <Button variant="contained" color="primary" className={"AddButton"}
                                onClick={e => this.setState({showAddForm: true})}>Add New Company
                        </Button>
                    </Box>

                </Box>
                <Box component="div" display="block">
                    {this.state.showAddForm &&
                    (
                        <form onSubmit={this.handleSubmit.bind(this)}>

                            <Box m={1}>
                                <InputLabel required={true} htmlFor="name">Company Name</InputLabel>
                                <Input required={true} type="text" id={"name"} value={this.state.formData.name}
                                       onChange={this.onInputChange.bind(this)}/>
                            </Box>
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
                            <Box m={1}>
                                <InputLabel  required={true} htmlFor="street">Street</InputLabel>
                                <Input  required={true} type="text" id={"street"} value={this.state.formData.street}
                                       onChange={this.onInputChange.bind(this)}/>
                            </Box>
                            <Box m={1}><InputLabel required={true} htmlFor="postalCode">Postal Code</InputLabel>
                                <Input required={true} type="text" id={"postalCode"} value={this.state.formData.postalCode}
                                       onChange={this.onInputChange.bind(this)}/></Box>
                            <Box m={1}>
                                <InputLabel required={true} htmlFor="monthlyRent">Monthly Rent</InputLabel>
                                <Input required={true} type="number" id={"monthlyRent"} value={this.state.formData.monthlyRent}
                                       onChange={this.onInputChange.bind(this)}/>
                            </Box>
                            <Box m={2}>
                                <Input  type="submit" value="Submit"/>
                            </Box>
                        </form>
                    )
                    }
                </Box>

            </Box>
        )
    }
};

const connnected = connect(mapStateToProps)(CompaniesList);

export default connnected