import React from 'react'
import ReactDOM from 'react-dom'
import { Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button, Row, Col } from 'reactstrap';

//import 'bootstrap/dist/css/bootstrap.css';
class Matches extends React.Component {
  constructor(props){
    super(props);
    this.state = {matches: [], loading: true}
  }
  async getMatches(){
    let matches = await fetch('/api/v1/matches');
    let json = await matches.json();
    this.setState({
      matches: json,
      loading: false,
    })
  }
  componentWillMount(){
    this.getMatches()
  }
  render () {
      if (this.state.loading){
        return <h1>LOADING</h1>
      }
      if (!this.state.loading){
        return <Row>{this.state.matches.map(item => <Match key={ item.match_id }
                            match={ item }/> )}</Row> ;
      }
  }
}

class Match extends React.Component {
  render () {
  return  (
    <Col md="12" lg="12" sm="12">
     <Card>
       <CardBody>
         <CardTitle>{ this.props.match.match_id }</CardTitle>
         <div align="center">
         <CardSubtitle>Radiant</CardSubtitle>
         <Teams match={this.props.match} team="radiant" />
         </div>
         <div>
         <CardSubtitle>Dire</CardSubtitle>
         <Teams match={this.props.match} team="dire" />
         </div>
       </CardBody>
     </Card>
   </Col>
 )
  }
}

class Teams extends React.Component {
  render () {
    return <div>{this.props.match[this.props.team].map(player =><Player hero={ player.hero } key={ player.hero }/> )} </div>;
  }
}

class Player extends React.Component {
  render() {
    return (
      <h2> { this.props.hero }</h2>
    )
  }
}

ReactDOM.render(
  <Matches />,
  document.getElementById('react')
);
