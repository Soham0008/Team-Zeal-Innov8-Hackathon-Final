import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import Card from './Card'
const CardSlider = () => {
  const cards = [
    { id: 1, title: 'Card 1', description: 'This is the first card.' },
    { id: 2, title: 'Card 2', description: 'This is the second card.' },
    { id: 3, title: 'Card 3', description: 'This is the third card.' },
  ];

  return (
    <Swiper
      spaceBetween={50}
      slidesPerView={1}
      loop={true} // Enable infinite loop
      navigation={true}
      modules={[Navigation]}
    >
      {cards.map(card => (
        <SwiperSlide key={card.id}>
          <Card id={card.id} title={card.title} description={card.description} />
        </SwiperSlide>
      ))}
    </Swiper>
  );
}

export default CardSlider;
