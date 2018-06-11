import React from 'react';
import ReactDOM from 'react-dom';
import { Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button, Row, Col, CardLink } from 'reactstrap';

class Players extends React.Component {
  constructor(props){
    super(props);
    this.state = {users: [], loading:true}

  }
  async getPlayers(){
    let players = await fetch('/api/v1/users');
    let json = await players.json()
    console.log(json)
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
    return <div align="center">{users.map(item => <Player key={item.pk}
                        personaname={item.personaname} img={item.avatarfull} /> )}</div>;
    }
  }
}

class Player extends React.Component {
  render() {
    return  (
      <Col md="6" lg="6" sm="6">
       <Card>
         <CardBody>
           <CardTitle>{ this.props.personaname }</CardTitle>
           <br /> <br />
           <img width="70%" src={ this.props.img } alt="Card image cap"/>
         </CardBody>
         <CardBody>
         <br /><br />
           <CardText>PROFILE DATA HERE </CardText>
           <br /> <br />
           <Row>
           <Col md="4" lg="4" sm="4">
           <CardLink href="#">Invite</CardLink>
           </Col>
           <Col md="4" lg="4" sm="4">
           <CardLink href="#">View Matches</CardLink>
           </Col>
           <Col md="4" lg="4" sm="4">
           <CardLink href="#">View Profile</CardLink>
           </Col>
           </Row>
         </CardBody>
       </Card>
     </Col>
   )
    }
}

ReactDOM.render(
  <Players />,
  document.getElementById('players')
)
