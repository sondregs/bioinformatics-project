import React from "react"
import {InputGroup, FormControl,  Button} from 'react-bootstrap'

import "../styles/SearchBar.css"

class SearchBar extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            hasTried: "not tried",
            isLoaded: "false",
            input: "",
            result: null,
            url: "www"
        };
      }

    go = () => {
        // let url = "http://127.0.0.1:8080/api/submit?sequence=" + this.state.input
        let url = "http://127.0.0.1:8080/api/submit"
        this.setState({url: url})
        fetch(url)
            .then(res => res.json())
            .then(
                (result) => {
                this.setState({
                    isLoaded: "true, win",
                    result: result
                });
                },
                // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
                // exceptions from actual bugs in components.
                (error) => {
                    console.log(error);
                    this.setState({
                        isLoaded: "true, fail",
                        error
                    });
                }
            )
    }

    handleChange = (e) => {
        this.setState({input: e.target.value})
    }

    handleSearch = () => {
        this.setState({input: ""})
    }


    // What does this component do?
    render () {
        return (
            <div class="SearchBar">
                <h2>INSERT SEQUENCE TO SEARCH:</h2>
                <div className="InputField">
                    <InputGroup size="lg" onChange={this.handleChange}>
                        <FormControl  aria-describedby="inputGroup-sizing-sm" />
                        <InputGroup.Append>
                            <Button variant="secondary" onClick={this.go}>
                                Search
                            </Button>
                        </InputGroup.Append>
                    </InputGroup>
                </div>
                <h3>{this.state.input}</h3>
                <h3>{this.state.isLoaded}</h3>
                <h3>{this.state.hasTried}</h3>
                <h3>{this.state.result}</h3>
                <h3>{this.state.url}</h3>
            </div>
        )
    }
}

export default SearchBar