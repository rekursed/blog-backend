import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import Navbar from './layout/Navbar'
import Homepage from './pages/Homepage'


class App extends Component {
    render() {
        return (
            <div>
                <Navbar/>
                <Homepage/>
            </div>

        )
    }
}
ReactDOM.render(<App/>, document.getElementById('react-app'))
