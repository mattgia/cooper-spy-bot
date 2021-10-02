import './app.css';
import Controls from './controls';

const app = () => {
  const { REACT_APP_STREAM_URL: streamUrl } = process.env;
  return (
    <div className="main">
      <img src={streamUrl} className="stream-image" alt="logo" />
      <Controls />
    </div >
  );
}

export default app;
