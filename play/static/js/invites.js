import React from 'react'
import ReactDOM from 'react-dom'
import {ListGroup, ListGroupItem, Button} from 'reactstrap'

class Invites extends React.Component {
  constructor(){
    super();
    this.state = {loading:true, invites: [], filter_type: {'from': 'View Sent', 'to': 'View Received'}, filter: 'from'}
    this.handleFilter = this.handleFilter.bind(this)
  }

  handleFilter(filter){
    this.setState({
      loading: true,
      filter: filter=='from' ? 'to':'from',
    })
    this.getInvites()
  }
  async getInvites(){
    // filter based on invites sent or received
    // the url would where the user wants to see all invites sent /api/v1/invites/?user_from=<thisUser>
    let invites = await fetch('/api/v1/invites/?user_'+this.state.filter+'='+window.props.user)
    let json = await invites.json()
    this.setState({
      loading:false,
      invites: json,
    })
  }
  async filter(){

  }
  componentWillMount(){
      this.getInvites()
  }
  render() {
    if (this.state.loading){
      return   <ListGroup>LOADING</ListGroup>
    } else{
      return (
        <div>
        <Button onClick={ () => this.handleFilter(this.state.filter)}>{this.state.filter_type[this.state.filter]}</Button>
        <Invite invite={this.state.invites} filter={this.state.filter}/>
        </div>
      )
    }
  }

}

class Invite extends React.Component{
  render(){
    return (
    <ListGroup>
      {this.props.invite.map(item => <ListGroupItem key={item.id}>{item.user_to_slug}<br />{item.status}</ListGroupItem>)}
    </ListGroup>
    )
  }
}
ReactDOM.render(
  <Invites />,
  document.getElementById('react')
);
