import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import Card from './Card'
import cards from '../final.json'

const CardSlider = () => {


  return (
    <Swiper
      spaceBetween={50}
      slidesPerView={1}
      loop={true} // Enable infinite loop
      navigation={true}
      modules={[Navigation]}
    >
      {cards.map(card => (
        <SwiperSlide key={card.candidate_id}>
          <Card id={card.candidate_id} title={card.name} rank={card.rank}/>
        </SwiperSlide>
      ))}
    </Swiper>
  );
}

export default CardSlider;
