// src/Sidebar.js
import React from 'react';
import styles from './Sidebar.module.css';
import { useNavigate } from 'react-router-dom';

const Sidebar = () => {

  const navigate = useNavigate();

  return (
    <div className={styles.sidebar}>
            <div className={styles.sidebarElement} onClick={() => navigate('/')}>Home</div>
            <div className={styles.sidebarElement} onClick={() => navigate('/dashboard')}>Dashboard</div>
            <div className={styles.sidebarElement} onClick={() => navigate('/analytics')}>Analytics</div>
        </div>
  );
};

export default Sidebar;
