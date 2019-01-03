import React, {PropTypes} from 'react';
import { Link, IndexLink } from 'react-router';
import LoadingDots from './LoadingDots';

const Header = ({loading}) => {
  return (
    <nav>
      <IndexLink to="/" activeClassName="active">⚽ Home</IndexLink>
      {" | "}
      <Link to="/games" activeClassName="active">⚽ Games</Link>
      {" | "}
      <Link to="/about" activeClassName="active">⚽ About</Link>
      {loading && <LoadingDots interval={100} dots={5}/>}
    </nav>
  );
};

Header.propTypes = {
  loading: PropTypes.bool.isRequired
};

export default Header;
