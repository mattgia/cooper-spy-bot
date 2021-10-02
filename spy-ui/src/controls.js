import axios from 'axios';
import debounce from 'lodash.debounce';

const { REACT_APP_MOTOR_CONTROLS_URL: controlsUrl } = process.env;

const move = (direction) =>
    axios.post(controlsUrl, {
        "method": direction,
        "params": [],
        "jsonrpc": "2.0",
        "id": 0
    }).catch(console.error);

const stop = () => move('stop');
const moveLeft = () => move('turn_left');
const moveRight = () => move('turn_right');
const moveForward = () => move('forward');
const moveBackward = () => move('backward');

const directions = {
    up: 'ArrowUp',
    down: 'ArrowDown',
    left: 'ArrowLeft',
    right: 'ArrowRight'
}

window.onkeydown = (e) => {
    if (e.repeat) {
        return;
    }
    if (e.code === directions.down) {
        moveBackward();
    } else if (e.code === directions.up) {
        moveForward();
    } else if (e.code === directions.right) {
        moveRight()
    } else if (e.code === directions.left) {
        moveLeft()
    }
}
window.onkeyup = (e) => {
    if (Object.values(directions).includes(e.code)) {
        stop()
    }
}

const controls = () => {
    return <></>
}


export default controls;
