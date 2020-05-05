import React, {Component} from 'react';
import logo from '../../../img/logo.png';
import './Navbar.scss'

class Navbar extends React.Component {
    render() {
        return (
            <nav id="navbar" className="navbar" role="navigation" aria-label="main navigation">
                <div className="navbar-brand">
                    <a className="navbar-item" href="/">
                      <span>
                        <img src={"static/dist/" + logo} alt="Mohammad Hassan"/>
                        <span className="brand-title is-hidden-mobile">Mohammad Hassan</span>
                      </span>
                    </a>
                </div>
                <a role="button" className="navbar-burger burger" aria-label="menu" aria-expanded="false"
                   data-target="rightNavBar">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </a>
                <div id="rightNavBar" className="navbar-menu">
                    <div className="navbar-end">
                        <a className="navbar-item">
                            About
                        </a>
                        <a className="navbar-item">
                            Articles
                        </a>
                    </div>
                </div>
            </nav>
        );
    }
}

export default Navbar;
