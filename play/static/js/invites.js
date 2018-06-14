import React from 'react'
import ReactDOM from 'react-dom'
import {ListGroup, ListGroupItem, Button, CardText,Card,CardBody, CardTitle, Col, Row, CardLink, CardSubtitle, CardImg} from 'reactstrap'

class Invites extends React.Component {
  constructor(){
    super();
    this.state = {loading:true, invites: [], filter_type: {'user_from': 'View Sent', 'user_to': 'View Received'}, filter: '', filtered:[]}
    this.handleFilter = this.handleFilter.bind(this)
  }

  async handleFilter(filter){
    await this.setState({
      filter: filter=='user_from' ? 'user_to':'user_from',
      filtered:[],
    })
    await this.state.invites.forEach(item => item[filter+'_slug']==window.props.user_slug ? this.setState({
      filtered: [...this.state.filtered, item],
    }) : null
  )
  }
  async getInvites(){
    // filter based on invites sent or received
    // the url would where the user wants to see all invites sent /api/v1/invites/?user_from=<thisUser>
    let invites = await fetch('/api/v1/invites/')
    let json = await invites.json()
    this.setState({
      invites: json,
      loading: false,
    })
    this.handleFilter('user_to')
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
        <Invite invite={this.state.filtered} filter={this.state.filter}/>
        </div>
      )
    }
  }

}

class Invite extends React.Component{
  constructor(){
    super();
    this.InviteAction = this.InviteAction.bind(this)
  }
  async InviteAction(action_type,id){
    console.log(action_type, id)
  }

  render(){
    return (
    <div>
      {this.props.invite.map(item =>
        <Col sm="4" key={item.id}>
        <Card align="center">
        <CardBody>
          <CardTitle>{item[this.props.filter+'_slug']}</CardTitle>
          <CardSubtitle></CardSubtitle>
          {this.props.filter=='user_from' ? <Row>
          <Col sm="6" md="6">
          <CardLink href="#" onClick={() => this.InviteAction('accept', item.id)}>Accept</CardLink>
          </Col>
          <Col sm="6" md="6">
          <CardLink href="#" onClick={() => this.InviteAction('decline', item.id)}>Decline</CardLink>
          </Col>
          </Row>:
           ''}
        </CardBody>
      </Card>
      </Col>
      )}
    </div>
    )
  }
}

ReactDOM.render(
  <Invites />,
  document.getElementById('react')
);
