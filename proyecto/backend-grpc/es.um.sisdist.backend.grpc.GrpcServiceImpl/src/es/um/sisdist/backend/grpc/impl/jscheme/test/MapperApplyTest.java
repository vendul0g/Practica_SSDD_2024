/**
 * 
 */
package es.um.sisdist.backend.grpc.impl.jscheme.test;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import es.um.sisdist.backend.grpc.impl.jscheme.MapperApply;
import jscheme.JScheme;
import static jscheme.JScheme.*;

/**
 * @author dsevilla
 *
 */
class MapperApplyTest
{
	static JScheme js;

	static class Wrap {
		int v = 0;
		
		void inc() {++v;}
		int get() {return v;}
	};
	
	/**
	 * @throws java.lang.Exception
	 */
	@BeforeAll
	static void setUpBeforeClass() throws Exception
	{
		js = new JScheme();
	}

	/**
	 * @throws java.lang.Exception
	 */
	@BeforeEach
	void setUp() throws Exception {
	}

	/**
	 * Test method for {@link es.um.sisdist.backend.grpc.impl.jscheme.MapperApply#apply_map_function(jscheme.SchemePair)}.
	 */
	@Test
	void testApply_map_functionSchemePair()
	{
		final Wrap w = new Wrap();
		
		MapperApply ma = new MapperApply(js, 
				"(define (ssdd_map p)"
				+ "(begin"
				+ " (display (first p))"
				+ " (display \": \")"
				+ " (display (second p))"
				+ " (emit (list (first p) (second p)))"
				+ "))",
				p ->  // emit function
					{
						System.out.println("Called: "
								+ p.first()
								+ ", "
								+ p.second());
						w.inc();
						return null;
					});

		ma.apply(list(3,4));
		assertEquals(w.get(), 1);
	}

	/**
	 * Test method for {@link es.um.sisdist.backend.grpc.impl.jscheme.MapperApply#apply_ssdd_map_function(java.lang.Object, java.lang.Object)}.
	 */
	@Test
	void testApply_map_functionT1T2() 
	{
	}

}
