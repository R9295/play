import React from 'react';
import ReactDOM from 'react-dom';
import { Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button, Row, Col, CardLink,ListGroup, ListGroupItem } from 'reactstrap';

class Players extends React.Component {
  constructor(props){
    super(props);
    this.state = {users: [], loading:true}
  }
  async getPlayers(){
    let players = await fetch('/api/v1/users');
    let json = await players.json()
    this.setState({
      users: json,
      loading: false,
    })
  }
    componentWillMount(){
      this.getPlayers()
    }
  render () {
    if (this.state.loading){
      return <h1>LOADING</h1>
    }
    if (!this.state.loading){
      let users = this.state.users
    return <div align="center"><Row>{users.map(item => <Player key={item.pk} id={item.pk}
                        personaname={item.personaname} img={item.avatarfull} profile={item.profile} /> )}</Row></div>;
    }
  }
}

class Player extends React.Component {
  constructor(props){
    super(props);
    this.invite = this.invite.bind(this);
    this.state = {id: this.props.id }
  }
  invite(){
    
  }
  render() {
    //this.props.profile.fav_servers.forEach(item => console.log(item))
    return  (
      <Col md="4" lg="4" sm="4">
       <Card>
         <CardBody>
           <CardTitle>{ this.props.personaname }</CardTitle>
           <br /> <br />
           <img width="70%" src={ this.props.img } alt="Card image cap"/>
         </CardBody>
         <CardBody>
         <br /><br />
          < FavObj name='Preferred Servers' data={this.props.profile.fav_servers} />
          < FavObj name='Preferred Heroes' data={this.props.profile.fav_heroes} />
          < FavObj name='Preferred Roles' data={this.props.profile.fav_roles} />
           <br /> <br />
           <Row>
           <Col md="6" lg="6" sm="6">
           <CardLink href="#" onClick={this.invite}>Invite</CardLink>
           </Col>
           <Col md="6" lg="6" sm="6">
           <CardLink href="#">View Matches</CardLink>
           </Col>
           </Row>
         </CardBody>
       </Card>
     </Col>
   )
    }
}
class FavObj extends React.Component {
  render(){
    return (
      <div>
      <h6 align="left">{this.props.name}</h6>
      <ListGroup>
        {this.props.data.map(item =><ListGroupItem key={item}>{item}</ListGroupItem>)}
      </ListGroup>
      </div>
    )
  }
}
ReactDOM.render(
  <Players />,
  document.getElementById('players')
)
