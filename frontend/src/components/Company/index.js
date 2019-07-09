import React from 'react'
import './index.css'
import Link from '@material-ui/core/Link';
import TableRow from "@material-ui/core/TableRow";
import TableCell from "@material-ui/core/TableCell";


const Company = props => {

    const {company} = props;
    return (
        <TableRow >
            <TableCell>{company.name}</TableCell>
            <TableCell>{company.city}</TableCell>
            <TableCell>{company.street}</TableCell>
            <TableCell>{company.postal_code}</TableCell>
            <TableCell><Link href={`/company/${company.id}`}>Show All Offices</Link></TableCell>
        </TableRow>
    )

};

export default Company