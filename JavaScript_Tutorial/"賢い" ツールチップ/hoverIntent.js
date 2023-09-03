'use strict';

// Here's a brief sketch of the class
// with things that you'll need anyway
class HoverIntent {

    constructor({
        sensitivity = 0.1, // speed less than 0.1px/ms means "hovering over an element"
        interval = 100, // measure mouse speed once per 100ms: calculate the distance between previous and next points
        elem,
        over,
        out
    }) {
        this.sensitivity = sensitivity;
        this.interval = interval;
        this.elem = elem;
        this.over = over;
        this.out = out;

        // make sure "this" is the object in event handlers.
        this.onMouseMove = this.onMouseMove.bind(this);
        this.onMouseOver = this.onMouseOver.bind(this);
        this.onMouseOut = this.onMouseOut.bind(this);

        // assign the handlers
        elem.addEventListener("mouseover", this.onMouseOver);
        elem.addEventListener("mouseout", this.onMouseOut);

        // continue from this point

    }

    onMouseOver(event) {
        if (this.isOverElement) return;

        this.isOverElement = true;

        this.prevX = event.pageX;
        this.prevY = event.pageY;
        this.prevTime = Data.now();

        elem.addEventListener('mousemove', this.onMouseMove);
        this.checkSpeedInterval = setInterval(this.trackSpeed, this.interval);
    }

    onMouseOut(event) {
        if (!event.relatedTarget || !elem.contains(event.relatedTarget)) {
            this.isOverElement = false;
            this.elem.removeEventListener('mousemove', this.onMouseMove);
            clearInterval(this.checkSpeedInterval);
            if (this.isHover) {
                this.out.call(this.elem, event);
                this.isHover = false;
            }
        }
    }

    onMouseMove(event) {
        this.lastX = event.pageX;
        this.lastY = event.pageY;
        this.lastTime = Date.now();
    }

    trackSpeed() {
        let speed;

        if (!this.lastTime || this.lastTime == this.prevTime) {
            speed = 0;
        } else {
            speed = Math.sqrt(Math.pow(this.prevX - this.lastX, 2)) / (this.lastTime - this.prevTime);
        }

        if (speed < this.sensitivity) {
            clearInterval(this.checkSpeedInterval);
            this.isHover = true;
            this.over.call(this.elem, event);
        } else {
            this.prevX = this.lastX;
            this.prevTime = this.lastTime;
        }
    }


    destroy() {
        elem.removeEventListener('mousemove', this.onMouseMove);
        elem.removeEventListener('mouseover', this.onMouseOver);
        elem.removeEventListener('mouseout', this.onMouseOut);
    };

}