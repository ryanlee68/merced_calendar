// import logo from './logo.svg';
import YoutubeEmbed from './components/YoutubeEmbed';
import InputForm from './components/InputForm'
import GitHubIcon from '@mui/icons-material/GitHub';
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import IconButton from '@mui/material/IconButton';
import './App.css';


function App() {
  return (
    <div className="App">
      *Only input classes that have a schedule*
      Follow the instructions from the video
      <div className="Joint">
        <YoutubeEmbed></YoutubeEmbed>
        <div className="Input">
          <InputForm></InputForm>
        </div>
      </div>
      Made with ❤️ by Ryan Lee
      <br></br>
      <IconButton href='https://github.com/ryanlee68/merced_calendar' target="_blank" rel="noopener noreferrer" aria-label="delete">
        <GitHubIcon />
      </IconButton>
      <IconButton href='https://www.linkedin.com/in/ryan-lee-6796681a6/' target="_blank" rel="noopener noreferrer" aria-label="delete">
        <LinkedInIcon />
      </IconButton>
    </div>
  );
}

export default App;
