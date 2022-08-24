import React, { useState } from "react";
// import PlusButton from './PlusButton';
import TextFields from './TextFields';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import AddIcon from '@mui/icons-material/Add';
import '../styling/InputForm.scss'

// const Input = () => {
//   return <input placeholder="Your input here" />;
// };

function InputForm() {
  
  const [inputList, setInputList] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const arrOfStr = data.getAll('crn');
    const arrOfNum = [];
    arrOfStr.forEach(str => {
      arrOfNum.push(Number(str));
    });
    console.log(arrOfNum)
  }

  const onAddBtnClick = event => {
    setInputList(inputList.concat(
    <React.Fragment>
      <TextFields key={inputList.length} />
    </React.Fragment>));
  };

  return (
    <Box className='Form' component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
      <TextFields></TextFields>
      {inputList}
      <IconButton onClick={onAddBtnClick} size="large" aria-label="delete">
        <AddIcon className='Button' fontSize="inherit" />
      </IconButton>
      <Button
        type="submit"
        variant="contained"
        sx={{ mt: 3, mb: 2 }}
      >
        Continue
      </Button>
    </Box>
  );
}

export default InputForm;