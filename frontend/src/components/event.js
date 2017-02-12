'use strict'
import React, {Component} from 'react'

export default class Event extends Component{

  constructor (props){
    super(props)
    this.state = {data:[]}
  }

  loadEvent(){
    fetch(this.props.url)
    .then(response => response.json())
    .then(data => this.setState({data:data}))
    .catch(err => console.log(this.props.url, err.toString()))
  }

  componentDidMount () {
    this.loadEvent()
  }

  render(){
    return (
      <h3>{this.state.data.name}</h3>
    )
  }

}
