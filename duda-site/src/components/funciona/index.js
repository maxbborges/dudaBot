import React from 'react'
import { Container, Row, Col, Carousel } from 'react-bootstrap'
import './func.css'

//impor img slid
import MicSlide from '../../assets/img/mic-slid.png'
import ChatSlide from '../../assets/img/chat-slid.png'
import TelegramSlide from '../../assets/img/telegram-slid.png'
import NotebookSlide from '../../assets/img/notebook-slid.png'

//import img icon
import mic from '../../assets/img/mic.png'
import telegram from '../../assets/img/telegram.png'
import chat from '../../assets/img/chat.png'
import notebook from '../../assets/img/notebook.png'

function Funciona(){
    return(
        <Container fluid className="funciona" id="funciona">

            <Row>
                <Col xs={12}  md={4} className="fun-title">
                    <h2>COMO FUNCIONA?</h2>
                    <p>O Educa² é simples e intuitivo, tanto para professores quanto para alunos. Cris, nossa assistente virtual, guiará todos os passos.</p>
                </Col>
                <Col md={4} className="d-none d-md-flex icon-func">
                        <img src={mic} />
                        <p>Professor entra em contato com a Cris, grava a aula em áudio mp3 e envia.</p>
                </Col>
                <Col md={4} className="d-none d-md-flex icon-func">
                        <img src={telegram} />
                        <p>O envio do arquivo de áudio é realizado via Telegram de forma interativa.</p>
                </Col>
                <Col md={4} className="d-none d-md-flex icon-func">
                        <img src={notebook} />
                        <p>A cada aula Recebida, a Cris enviará um sms para os alunos indicados pelo professor.</p>
                </Col>
                <Col md={4} className="d-none d-md-flex icon-func">
                        <img src={chat} />
                        <p>A mensagem conterá dados basicos da aula em um número telefônico para que os alunos tenham acesso ao conteúdo.</p>
                </Col>
            </Row>

            <Row className="d-md-none">
            <Carousel className="slid-container">
                    <Carousel.Item>
                        <img
                        className="d-block w-100"
                        src={MicSlide}
                        alt="Missão"
                        />
                        <Carousel.Caption>
                            <p>Professor entra em contato com a Cris, grava a aula em áudio mp3 e envia.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                        className="d-block w-100"
                        src={TelegramSlide}
                        alt="Missão"
                        />
                        <Carousel.Caption>
                            <p>O envio do arquivo de áudio é realizado via Telegram de forma interativa.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                        className="d-block w-100"
                        src={NotebookSlide}
                        alt="Missão"
                        />
                        <Carousel.Caption>
                            <p>A cada aula Recebida, a Cris enviará um sms para os alunos indicados pelo professor.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                        className="d-block w-100"
                        src={ChatSlide}
                        alt="Missão"
                        />
                        <Carousel.Caption>
                            <p>A mensagem conterá dados basicos da aula em um número telefônico para que os alunos tenham acesso ao conteúdo.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                </Carousel>
            </Row>
        </Container>
    )
}

export default Funciona