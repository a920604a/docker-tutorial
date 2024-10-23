import logo from './logo.svg';
import './App.css';
import FaceDetectionApp from './FaceDetectionApp.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <FaceDetectionApp />
      </header>
    </div>
  );
}

export default App;
