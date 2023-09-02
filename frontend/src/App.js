import React, {useState} from 'react';
import './App.css';
import {Button, TextField} from "@mui/material";
import {DatePicker, LocalizationProvider} from "@mui/x-date-pickers";
import {AdapterDayjs} from "@mui/x-date-pickers/AdapterDayjs";


function App() {

  const [travelTo, setTravelTo] = useState('');
  const [travelFrom, setTravelFrom] = useState('');
  const [avStart, setAvStart] = useState(null);
  const [avEnd, setAvEnd] = useState(null);
  const [duration, setDuration] = useState('');


  return (
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <header className="App-header">
        </header>
        <div className="App-buttons">
          <TextField
              label="Travelling To..."
              variant="outlined"
              value={travelTo}
              onChange={(e) => setTravelTo(e.target.value)}
          />
          <TextField
              label="Travelling From..."
              variant="outlined"
              value={travelFrom}
              onChange={(e) => setTravelFrom(e.target.value)}
          />
          <DatePicker
              label="Availability (start)"
              value={avStart}
              onChange={setAvStart}
          />
          <DatePicker
              label="Availability (end)"
              value={avEnd}
              onChange={setAvEnd}
          />
          <TextField
              id="duration" label="Duration" variant="outlined"
              value={duration}
              onChange={(e) => setDuration(e.target.value)}

          />
          <Button variant="contained" color="secondary">
            Search
          </Button>

        </div>

      </LocalizationProvider>

  );
}

export default App;
