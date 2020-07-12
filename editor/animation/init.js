//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function triagularIslandsVisualization(tgt_node, data) {

            if (! data || ! data.ext) {
                return
            }

            const input = data.in
            const explanation = data.ext.explanation
            const answer = data.ext.answer

            /*----------------------------------------------*
             *
             * attr
             *
             *----------------------------------------------*/
            const attr = {
                triangle: {
                    none: {
                        'stroke': '#666666',
                        'stroke-width': '0.2px',
                        'fill': '#dfe8f7',
                    },
                    lit: {
                        'fill': '#ffc965',
                        'stroke': '#666666',
                        'stroke-width': '0.2px',
                    },
                },
            }

            /*----------------------------------------------*
             *
             * values
             *
             *----------------------------------------------*/
            const grid_size_px = 300
            const os_t = grid_size_px * 0.1

            /*----------------------------------------------*
             *
             * paper
             *
             *----------------------------------------------*/
            const paper = Raphael(tgt_node, grid_size_px, grid_size_px, 0, 0)

            /*----------------------------------------------*
             *
             * draw triangles
             *
             *----------------------------------------------*/
            const max_number = Math.max(...input, 9)
            let rows = 1
            while (true) {
                if (Math.pow(rows, 2) >= max_number) {
                    break
                }
                rows += 1
            }

            const height = grid_size_px / rows * 0.8
            const edge = height / Math.sqrt(3) * 2
            let number = 1

            for (let r = 0; r < rows; r += 1) {
                let start_y = r * height + os_t
                let start_x = grid_size_px / 2 - (edge / 2 * r)
                for (let c = 0; c < r*2+1; c += 1) {
                    paper.path(['M', start_x, start_y + height * (c % 2),
                                'l', -edge/2, edge/2 * Math.sqrt(3) * (c % 2 ? -1 : 1),
                                'l', edge, 0,
                                'z']).attr(attr.triangle[input.includes(number) ? 'lit' : 'none'])

                    paper.text(
                        start_x,
                        start_y + height / 2 + (c % 2 ? -8 * (2/rows) : 8 * (2/rows)),
                        number
                    ).attr({'font-size': 30 * (2/rows)})

                    start_x += edge / 2
                    number += 1
                }
            }
        }

        var $tryit;

        var io = new extIO({
            multipleArguments: false,
            functions: {
                python: 'triangular_islands',
                js: 'triangularIslands'
            },
            animation: function($expl, data){
                triagularIslandsVisualization(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
