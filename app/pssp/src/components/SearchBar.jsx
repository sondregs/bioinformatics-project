import React from "react"
import {InputGroup, FormControl,  Button, Container} from 'react-bootstrap'

import "../styles/SearchBar.css"

class SearchBar extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoaded: false,
            input: "",
            result: null,
            primary_structure: "",
            secondary_structure: "",
            status: "cool"
        };
      }

    go = () => {
        // let url = "http://127.0.0.1:8080/api/submit?sequence=" + this.state.input
        let url = "http://127.0.0.1:8080/api/submit"
        fetch(url)
            .then(res => res.json())
            .then(
                (result) => {
                this.setState({
                    isLoaded: true,
                    result: result,
                    primary_structure: result.primary_structure,
                    secondary_structure: result.secondary_structure
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
                <h4>Primary structure:</h4>
                <h3>{this.state.primary_structure}</h3>

                <h4>Secondary structure:</h4>
                <h3>{this.state.secondary_structure}</h3>
            </div>
        )
    }
}

export default SearchBar