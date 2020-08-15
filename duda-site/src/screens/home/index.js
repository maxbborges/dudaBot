import React from 'react'

//import components
import Navbar from '../../components/navbar'
import Banner from '../../components/banner'
import Sobre from '../../components/sobre'
import Institucional from '../../components/Institucional'
import Funciona from '../../components/funciona'
import Surgiu from '../../components/surgiu'
import Somos from '../../components/somos'

function Home(){
    return(
        <>
            <Navbar />
            <Banner />
            <Sobre />
            <Institucional />
            <Funciona />
            <Surgiu />
            <Somos />
        </>
    )
}

export default Home