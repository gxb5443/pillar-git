/* eslint-disable no-script-url */

import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

import Typography from '@material-ui/core/Typography';

function Title(props) {
    return (
        <Typography component="h2" variant="h6" color="primary" gutterBottom>
            {props.children}
        </Typography>
    );
}

export default function Stats({ stars, forks, repo_name }) {
    return (
        <React.Fragment>
            <Title>Github Stats</Title>
            <Table size="small">
                <TableHead>
                    <TableRow>
                        <TableCell>Stat</TableCell>
                        <TableCell>Count</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    <TableRow>
                        <TableCell>Repo Name</TableCell>
                        <TableCell>{repo_name}</TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell>Stars</TableCell>
                        <TableCell>{stars}</TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell>Forks</TableCell>
                        <TableCell>{forks}</TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </React.Fragment>
    );
}