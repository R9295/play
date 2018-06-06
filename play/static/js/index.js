import React from 'react'
import ReactDOM from 'react-dom'
import { Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button, Row, Col } from 'reactstrap';
//import 'bootstrap/dist/css/bootstrap.css';

class Matches extends React.Component {
  render () {
    let matches = window.props;
    console.log(window.props)
    return <Row>{matches.map(item => <Match key={item.match_id}
                        match_id={item.match_id}/> )}</Row> ;
  }
}

class Match extends React.Component {
  render () {
  return  (
    <Col md="12" lg="12" sm="12">
     <Card>
       <CardBody>
         <CardTitle>{ this.props.match_id}</CardTitle>
         <CardSubtitle>Card subtitle</CardSubtitle>
         <CardText>"Some quick example text to build on the card title and make up the bulk of the card's content"</CardText>
         <Button>Button</Button>
       </CardBody>
     </Card>
   </Col>
 )
  }
}

ReactDOM.render(
  <Matches />,
  document.getElementById('react')
);
