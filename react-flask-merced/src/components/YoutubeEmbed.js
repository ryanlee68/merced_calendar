import React from "react";
import PropTypes from "prop-types";
import '../styling/YoutubeEmbed.scss'

const YoutubeEmbed = () => (
  <div className="video-responsive">
    <iframe
      src={`https://www.youtube.com/embed/vHKP6vaNlNY`}
      frameBorder="0"
      allowFullScreen
      title="Embedded youtube"
    />
  </div>
);

export default YoutubeEmbed;