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
            secondary_list: null,
            validated: false
        }
    }

    handleSubmit = () => {
        // Prod:
        // let url = "/api/submit?sequence=" + this.state.input
        // Dev:
        let url = "http://127.0.0.1:8080/api/submit?sequence=" + this.state.input
        fetch(url)
            .then(res => res.json())
            .then(
                (result) => {
                this.setState({
                    isLoaded: true,
                    result: result,
                    primary_structure: result.primary_structure,
                    secondary_structure: result.secondary_structure,
                    secondary_list: result.secondary_list,
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
        let value = e.target.value
        this.setState({input: value})
        if (value.length >= 20) {
            this.setState({
                validated: true,
            })
        } else {
            this.setState({validated: false})
        }
    }


    // What does this component do?
    render () {
        let pviz_link = "";
        if (this.state.secondary_list){
            let pviz_url = "/pviz/pviz.html" + "?primary=" + this.state.primary_structure + "&secondary=" + encodeURIComponent(JSON.stringify(this.state.secondary_list));
            pviz_link = <a href={pviz_url}>Click for Secondary Structure Visualization</a>
        }
        else {
            pviz_link = ""
        }
        return (
            <div class="SearchBar">
                <h2>INSERT SEQUENCE TO SEARCH:</h2>
                <div className="InputField">
                    <InputGroup size="lg" onChange={this.handleChange}>
                        <FormControl  aria-describedby="inputGroup-sizing-sm" />
                        <InputGroup.Append>
                            <InputGroup.Text variant="outline-secondary" >
                                {this.state.input.length}
                            </InputGroup.Text>
                        </InputGroup.Append>
                        <InputGroup.Append>
                            <Button variant="secondary" onClick={this.handleSubmit} disabled={!this.state.validated} >
                                Search
                            </Button>
                        </InputGroup.Append>
                    </InputGroup>

                    <p className="InfoText"> 
                        The sequence must be 20 characters or longer
                    </p>
                </div>
                <h4>Primary structure:</h4>
                <h3>{this.state.primary_structure}</h3>

                <h4>Secondary structure:</h4>
                <h3>{this.state.secondary_structure}</h3>

                <h4>Secondary structure visualization:</h4>
                <h3>{pviz_link}</h3>
            </div>
        )
    }
}

export default SearchBar