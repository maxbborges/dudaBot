import React from 'react'
import {Link} from 'react-router-dom'
import { Container, Row, Col } from 'react-bootstrap'
import './banner.css'

import IconBlue from '../../assets/icons/educa-blue.png'
import IconGreen from '../../assets/icons/educa-green.png'

function onClick(){
    window.location.href="http://url.com";
}

function Banner(){
    return(
        <Container fluid className="banner" id="banner" >
            <Row className="d-lg-none " >
                <Col>
                    <img src={IconBlue} alt="Educa²" className="icon-blue" />
                </Col>
            </Row>
            <Row>
                <Col>
                    <h2 className="title-banner" >EDUCAÇÃO ACESSÍVEL</h2>
                </Col>
            </Row>
            <Row>
                <Col>
                    <p className="banner-text" >Conectando alunos e professores de forma simples e democratica</p>
                </Col>
            </Row>
            <Row>
                <Col>
                    <a target='_blank' href='https://wa.me/5521995018388?text=Olá Juliana do Educa2!'>
                        <button className="btn-contato">FALE COM A GENTE</button>
                    </a>
                </Col>
            </Row>
            <Row className="d-none d-lg-block" >
                <Col>
                    <img src={IconGreen} alt="Educa²" className="icon-green" />
                </Col>
            </Row>
        </Container>
    )
}

export default Banner