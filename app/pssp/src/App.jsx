import React, { Component } from 'react'

import HeaderBar from "./components/HeaderBar"
import SearchBar from "./components/SearchBar"

import "./styles/App.css"

class App extends Component {
    render() {
        return (
            <div className="App">
                <HeaderBar></HeaderBar>
                <SearchBar></SearchBar>
            </div>
        )
    }
}

export default App