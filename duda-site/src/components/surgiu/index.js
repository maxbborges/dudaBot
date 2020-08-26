import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'
import './surgiu.css'

//import img 
import book from '../../assets/img/book.png'
import aluno from '../../assets/img/aluno.png'
import map from '../../assets/img/map.png'

function Surgiu(){
    return(
        <Container fluid className="surgiu" id="surgiu" >
            <Row>
                <Col xs={{ span: 6, offset: 3 }} >
                    <h2>COMO SURGIU?</h2>
                </Col>
            </Row>
            <Row className="icons">
                <Col xs={12} md={4}>
                    <img src={book} />
                    <p>NECESSIDADE DE DEMOCRATIZAÇÃO DO ENSINO</p>
                </Col>
                <Col xs={12} md={4}>
                    <img src={aluno} />
                    <p>SEM DISTINÇÃO DE NÍVEL SOCIOECONÔMICO</p>
                </Col>
                <Col xs={12} md={4}>
                    <img src={map} />
                    <p>INDIFERENTE DA LOCALIZAÇÂO GEOGRÁFICA</p>
                </Col>
            </Row>
        </Container>
    )
}

export default Surgiu