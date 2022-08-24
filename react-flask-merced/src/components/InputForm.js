import React, { useState } from "react";
// import PlusButton from './PlusButton';
import TextFields from './TextFields';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import AddIcon from '@mui/icons-material/Add';
import '../styling/InputForm.scss';
// import { useNavigate } from "react-router-dom";
import axios from "axios";

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
    // window.open('/getcsv?data='+arrOfNum, '_blank');
    // axios.post('/getcsv', {
    // crns: arrOfNum
    // })
    // .then(function (response) {
    //   console.log(response);
    // })
    // .catch(function (error) {
    //   console.log(error);
    // });
    fetch('/getcsv', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({'crns': arrOfNum})
    })
    .then((response) => response.blob())
    .then((blob) => {
      // Create blob link to download
      const url = window.URL.createObjectURL(
        new Blob([blob]),
      );
      const link = document.createElement('a');
      link.href = url;
      // link.target = _self;
      // link.setAttribute('target', '_self');
      link.setAttribute(
        'download',
        `classes.csv`,
      );

      // Append to html link element page
      // document.body.appendChild(link);

      // Start download
      link.click();
      
      // Clean up and remove the link
      // link.parentNode.removeChild(link);
      // window.close();
      // const navigate = useNavigate();
      // navigate("/");
      // window.location.reload(false);
    });
  };
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