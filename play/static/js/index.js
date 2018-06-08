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
    let matches = await fetch('/matches');
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
    console.log(this.state)
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
         <Teams match = {this.props.match} team="radiant" />
         </div>
         <div>
         <CardSubtitle>Dire</CardSubtitle>
         <CardText>"Some quick example text to build on the card title and make up the bulk of the card's content"</CardText>
         </div>
       </CardBody>
     </Card>
   </Col>
 )
  }
}

class Teams extends React.Component {
  render () {
    return (
      <div>
      <script>
      console.log('123')
      </script>

      </div>
    )
  }
}
ReactDOM.render(
  <Matches />,
  document.getElementById('react')
);
