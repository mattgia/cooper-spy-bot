import './App.css';

function App() {
  const { REACT_APP_STREAM_URL: streamUrl } = process.env;
  return (
    <div className="main">
      <img src={streamUrl} className="stream-image" alt="logo" />
    </div>
  );
}

export default App;
