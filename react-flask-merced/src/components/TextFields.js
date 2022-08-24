import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

export default function TextFields() {
  return (
    <TextField
      // error={companyNameError}
      margin="normal"
      required
      fullWidth
      // id="email"
      label="CRN #"
      name="crn"
      autoFocus
      inputProps={{ maxLength: 40 }}
    />
  );
}